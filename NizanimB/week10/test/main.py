from content import Content
from viewer import Viewer
from creator import Creator
from platformmanager import PlatformManager

# Create objects
c1 = Content("Movie A", "Alice", "Action")
c2 = Content("Movie B", "Bob", "Drama")

v1 = Viewer(1, "Daniel")
cr1 = Creator(2, "Sarah")
pm1 = PlatformManager(3, "Manager G")


# ---------- Content ----------
c1.add_view()
c1.add_view()
c1.add_rating(4)
c1.add_rating(2)
c1.add_rating(5)
c1.set_genre("Comedy")
c1.print_details()


# ---------- Viewer ----------
v1.watch_content(c1)
v1.watch_content(c2)
v1.rate_content(c1, 5)
v1.rate_content(c2, 3)
v1.print_details()


# ---------- Creator ----------
cr1.upload_content(c1)
cr1.upload_content(c2)
cr1.print_details()


# ---------- Platform Manager ----------
pm1.add_creator(cr1)
pm1.upload_content(c1)
pm1.upload_content(c2)
pm1.print_details()