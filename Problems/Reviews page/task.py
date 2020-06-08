from django.shortcuts import render
from django.views import View


class ReviewView(View):
    template_name = 'book/reviews.html'
    reviews = ["asffd", "sdfsds", "sdfsdfsdf"]  # List of reviews as plain strings

    def get(self, request, *args, **kwargs):
        self.reviews.append("kjhlkjhlkj")
        return render(request, 'book/reviews.html', context={'reviews': self.reviews})