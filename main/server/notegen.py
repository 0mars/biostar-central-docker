"""
This module can generate messages
"""
from main.server.const import *

def userlink(user):
    return '[%s](%s)' % (user.profile.display_name, user.profile.get_absolute_url() )

def postlink(post, size=35):
    root  = post.root or post
    title = root.title if len(root.title) < size else '%s...' %  root.title[:size] 
    return '%s:[%s]( %s)' % (post.get_type_display(), title, post.get_absolute_url())

def badgelink(badge):
    return '[%s](%s)' % (badge.name, badge.get_absolute_url() )

def post_moderator_action(user, post):
    action = post.get_status_display()
    text   = '%s set status to %s on %s' % (userlink(user), action, postlink(post))
    return text

def user_moderator_action(user, target):
    action = target.profile.get_status_display()
    text   = '%s set status %s on %s' % (userlink(user), action, userlink(target))
    return text

def post_action(user, post, size=250):
    post_type = int(post.type)
    action = 'posted'
    if len(post.content) < size:
        content = post.content
    else:
        content = '%s...' % post.content[:size]
    text   = '%s %s %s: %s' % (userlink(user), action, postlink(post), content)
    return text

def awardnote(badge):
    text = "Congratulations! You've just earned the **%s** badge!" % badgelink(badge)
    return text