from WikiHandler import WikiHandler
from lib.db.Page import Page, add_page, age_set

class WikiEditPage(WikiHandler):
    def done(self, page="", path="", age=""):
        if not self.user:
            self.redirect("/wiki/login")
        self.render("editpage.html", path = path, page = page)

    def post(self, path):
        if not self.user:
            self.error(400)
            return

        content = self.request.get('content')
        author = self.user.name
        old_page = Page.by_path(path).get()

        if not(old_page or content):
            return
        elif not old_page or old_page.content != content:
            p = Page(parent = Page.parent_key(path), content = content, author = author)
            add_page(path, p)
            page_key = 'PAGE_' + path
            age_set(page_key, p)

        self.redirect('/wiki' + path)