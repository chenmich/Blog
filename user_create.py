import Blog as blog


admin_role = blog.models.user.Role.query.filter_by(
    rolename=blog.models.user.role_name.admin
).all()[0]
common_role = blog.models.user.Role.query.filter_by(
    rolename=blog.models.user.role_name.common).all()[0]
moderate_role = blog.models.user.Role.query.filter_by(
    rolename=blog.models.user.role_name.moderator).all()[0]
anonymous_role = blog.models.user.Role.query.filter_by(
    rolename=blog.models.user.role_name.anonymous).all()[0]

micheal = blog.models.user.User(
    username='micheal',
    email='micheal@163.com',
    password='111111',
    role=admin_role
)

lrq = blog.models.user.User(
    username='lrq',
    email='lrq@163.com',
    password='111111',
    role=admin_role
)

kfl = blog.models.user.User(
    username='kfl',
    email='kfl@163.com',
    password='111111',
    role=admin_role
)

zyq = blog.models.user.User(
    username='zyq',
    email='zyq@163.com',
    password='111111',
    role=admin_role
)

zl = blog.models.user.User(
    username='zl',
    email='zl@163.com',
    password='111111',
    role=moderate_role
)

ny = blog.models.user.User(
    username='ny',
    email='ny@163.com',
    password='111111',
    role=moderate_role
)

lzj = blog.models.user.User(
    username='lzj',
    email='lzj@163.com',
    password='111111',
    role=common_role
)

some = blog.models.user.User(
    username='some',
    email='some@163.com',
    password='111111'
)
print(micheal.verify_password('111111'))


blog.db.session.add_all(
    [micheal, lrq, kfl, zyq, zl, ny, lzj, some])
blog.db.session.commit()


#all_user = blog.models.user.User.query.filter_by(username='micheal').all()
#print(all_user)

#print(blog.models.user.user.user_loader('some'))
