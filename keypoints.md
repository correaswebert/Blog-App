- Project is divided into multiple apps, each with its own usecase.
  So our main project can be divided into multiple apps like a blog
  app, store app, etc.

- When we search for url from our main project, it tries to match it
  in the order of the urlpatterns list
  If a match is found, then site is redirected to that app and the
  matched portion of the url is trimmed before the app tries to do
  the same with its urlpatterns to redirect to the views (webpage).
