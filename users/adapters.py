from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    #new user
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        user.google_sub = sociallogin.account.uid  
        user.name = data.get("name") or ""
        return user
    #link user
    def pre_social_login(self, request, sociallogin):
        super().pre_social_login(request, sociallogin)
        user = sociallogin.user
        if user.pk and not user.google_sub:
            user.google_sub = sociallogin.account.uid
            if not user.name:
                user.name = sociallogin.account.extra_data.get("name", "")
            user.save(update_fields=["google_sub", "name"])