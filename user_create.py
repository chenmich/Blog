import Blog as blog

admin_role = blog.models.user.Role.query.filter_by(
    rolename=blog.models.user.role_name.admin).all()

admin_user = blog.models.user.User(
    username="chenmich",
    email='403189920@qq.com',
    password='chen620713',
    role=admin_role[0]
)

blog.db.session.add(admin_user)
blog.db.session.commit()