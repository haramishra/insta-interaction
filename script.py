

from instapy import InstaPy
from instapy import smart_run
# from instapy import set_workspace

# set_workspace(path="/home/hp/Documents/vegan/")


# get a session!
session = InstaPy(username='', password='')

photo_comments = ['looks amazing!',
                  'I love your profile!',
                  'Your feed is an inspiration :thumbsup:',
                  'Just incredible :open_mouth:',
                  'Love your posts',
                  'Looks awesome ',
                  ':heart::heart::heart:',
                  ':heart_eyes::heart_eyes::heart_eyes:',
                  ':thumbsup::thumbsup::thumbsup:',
                  'so beautiful']

# let's go! :>
with smart_run(session):
    # settings
    session.set_user_interact(amount=3, randomize=False, percentage=100,
                              media='Photo')
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    min_followers=50,
                                    min_following=50)
    session.set_simulation(enabled=False)
    session.set_do_like(enabled=True, percentage=100)
    # session.set_ignore_users([])
    session.set_do_comment(enabled=True, percentage=35)
    session.set_do_follow(enabled=True, percentage=55)
    session.set_comments(photo_comments)
    session.set_ignore_if_contains([])
    # session.set_action_delays(enabled=False, like=40)

    # activity
    session.interact_user_followers(['vegan'], amount=340)

    """ Joining Engagement Pods..."""
    session.join_pods(topic='food', engagement_mode='no_comments')
