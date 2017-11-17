import Blog as blog
blog.db.drop_all()
blog.db.create_all()

admin_role = blog.models.user.Role(rolename='Administrator')


follow_permission = blog.models.user.Permission(permission='FOLLOW')
comment_permission = blog.models.user.Permission(permission='COMMENT')
writeing_permission = blog.models.user.Permission(permission='WRITING')
moderate_comment_permission = blog.models.user.Permission(permission='MODERATE_COMMENT')
admin_permission = blog.models.user.Permission(permission='ADMINSTER')



blog.db.session.add(admin_role)
blog.db.session.add(follow_permission)
blog.db.session.add(comment_permission)
blog.db.session.add(writeing_permission)
blog.db.session.add(moderate_comment_permission)
blog.db.session.add(admin_permission)

blog.db.session.commit()

print(admin_role.id)
print(follow_permission.id)


