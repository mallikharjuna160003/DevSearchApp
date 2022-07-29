from django.shortcuts import render
from .models import Profile
# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request,'users/profiles.html',context)

def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    topskills = profile.skill_set.exclude(description__exact=None)
    otherskills = profile.skill_set.filter(description=None)
    context = {'profile':profile,'topskills':topskills,'otherskills':otherskills}
    print(topskills)
    return render(request,'users/user-profile.html',context)