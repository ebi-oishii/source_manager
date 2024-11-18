from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.db.models import Max
from .models import Project, Post, PapersIndices
from .forms import AddMemberForm
from papers.models import Paper
from django.urls import reverse_lazy


# Create your views here.

class CreateProjectView(CreateView):
    model = Project
    template_name = "research_projects/create_project.html"
    fields = ["name", "description", "project_url"]
    
    def get_success_url(self):
        # success_url を動的に取得して返す
        return reverse_lazy('research_projects:project_detail', kwargs={'project_id': self.object.project_id})
    
    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        
        project.members.add(self.request.user)

        return super().form_valid(form)
    
create_project = CreateProjectView.as_view()

class ProjectDetailView(DetailView):
    model = Project
    template_name = "research_projects/project_detail.html"
    context_object_name = "project"

    def get_object(self, queryset=None):
        # URLからproject_idを取得して、それを元にProjectオブジェクトを取得
        project_id = self.kwargs.get('project_id')
        return get_object_or_404(Project, project_id=project_id)

project_detail = ProjectDetailView.as_view()


class AddMemberView(UpdateView):
    model = Project
    template_name = "research_projects/add_member.html"
    form_class = AddMemberForm

    def get_project(self):
        project_id = self.kwargs.get("project_id")
        return get_object_or_404(Project, project_id=project_id)
    
    def get_object(self):
        return self.get_project()

    def get_success_url(self):
        project = self.get_project()
        return reverse_lazy('research_projects:project_detail', kwargs={'project_id': project.project_id})

add_member = AddMemberView.as_view()


class AddPostView(CreateView):
    model = Post
    template_name = "research_projects/add_post.html"
    fields = ["content"]

    def get_project(self):
        project_id = self.kwargs.get("project_id")
        return get_object_or_404(Project, project_id=project_id)

    def get_success_url(self):
        project = self.get_project()
        return reverse_lazy('research_projects:project_detail', kwargs={"project_id": project.project_id})

    def form_valid(self, form):
        post = form.save(commit=False)
        post.contributer = self.request.user
        post.project = self.get_project()
        post.save()
        return super().form_valid(form)
    
add_post = AddPostView.as_view()


class AddPaper(CreateView):
    model = PapersIndices
    fields = ["paper",]
    template_name = "research_projects/add_paper.html"

    def get_project(self):
        project_id = self.kwargs.get("project_id")
        return get_object_or_404(Project, project_id=project_id)

    def get_success_url(self):
        project = self.get_project()
        return reverse_lazy('research_projects:project_detail', kwargs={"project_id": project.project_id})

    def form_valid(self, form):
        paper_index = form.save(commit=False)
        project = self.get_project()
        paper_index.project = project
        i = PapersIndices.objects.filter(project=project).aggregate(Max("index"))["index__max"]
        if i is None:
            i = 1
        else:
            i += 1
        paper_index.index = i
        paper_index.save()
        return super().form_valid(form)
    
add_paper = AddPaper.as_view()


class EditCitationView(UpdateView):
    model = PapersIndices
    fields = ["description"]
    template_name = "research_projects/edit_citation.html"

    def get_project(self):
        project_id = self.kwargs.get("project_id")
        project = get_object_or_404(Project, project_id=project_id)
        return project

    def get_object(self):
        project = self.get_project()
        index = self.kwargs.get("index")
        paper_index = get_object_or_404(PapersIndices, project=project, index=index)
        return paper_index
    
    def get_success_url(self):
        project = self.get_project()
        return reverse_lazy('research_projects:project_detail', kwargs={"project_id": project.project_id})
    
edit_citation = EditCitationView.as_view()


class ProjectListView(ListView):
    template_name = "research_projects/project_list.html"
    context_object_name = "projects"
    queryset = Project.objects.filter(is_public=True)
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['numbers'] = [1, 2, 3, 4]  # 配列をコンテキストに追加
        return context

project_list = ProjectListView.as_view()