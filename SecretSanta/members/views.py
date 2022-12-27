from django.shortcuts import render, redirect
from django.views import View

from .models import *

def all_members(request):
    members = Member.objects.all()

    context = { 'members' : members }
    return render(request, 'members/all_members.html', context)


#-------------------------------------------------------------------------------------------------------------
#Members - CBV - Read and Create
class MemberList(View):

    def get(self, request):
        members  = Member.objects.all().order_by('-created_at')

        context = { 'members' : members }
        return render(request, 'members/all_members.html', context)


    def post(self, request):
        member = Member.objects.create(
                                        first_name = request.POST.get('first_name'),
                                        last_name  = request.POST.get('last_name'),
                                        email      = request.POST.get('email')
                                      )
        member.save()
        return redirect('members')


#-------------------------------------------------------------------------------------------------------------
#Members - CBV - Read-Detail-View and Update
class MemberDetail(View):
    def get(self, request, pk):
        member = Member.objects.get(id=pk)

        context = { 'member' : member }
        return render(request, 'members/member_detail.html', context)

    def post(self, request, pk):
        member            = Member.objects.get(id=pk)
        member.first_name = request.POST.get('first_name')
        member.last_name  = request.POST.get('last_name')
        member.email      = request.POST.get('email')

        member.save()
        return redirect('members')


#-------------------------------------------------------------------------------------------------------------
#Members - CBV - Delete
class MemberDelete(View):
    def get(self, request, pk):
        member = Member.objects.get(id=pk)

        context = { 'member' : member }
        return render(request, 'members/member_delete.html', context)

    def post(self, request, pk):
        member = Member.objects.get(id=pk)
        member.delete()
        return redirect('members')