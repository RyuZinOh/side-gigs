from github_api import get_data, unfollow_user, FOLLOWERS_API, FOLLOWING_API
from file_utils import save_json, load_json, save_not_following_back
from datetime import datetime

def track_changes():
    # Load previous data
    prev_data = load_json('github_data.json')
    prev_followers = set(prev_data.get('followers', []))
    prev_following = set(prev_data.get('following', []))

    # Fetch current followers and following
    current_followers = set(get_data(FOLLOWERS_API))
    current_following = set(get_data(FOLLOWING_API))

    # Identify users not following back
    not_following_back = current_following - current_followers

    # Save the list of users not following back
    save_not_following_back('out.txt', not_following_back)

    # Unfollow users not following back
    for user in not_following_back:
        unfollow_user(user)

    # Save the current data for future reference
    save_json('github_data.json', {
        'followers': list(current_followers),
        'following': list(current_following),
        'last_checked': datetime.now().isoformat()
    })

if __name__ == "__main__":
    track_changes()
