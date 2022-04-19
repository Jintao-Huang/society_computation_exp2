# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
1G:
2. Member_id List
3. Event_id List
5. Topic_id List
- Organizer_id(2. M)

2M:
1. Group_id List
3. Event_id List
4. RSVP_id List
5. Topic_id List
- Organize_Group(1. G)

3E:
1. Group_id
2. Member_id List
4. RSVP_id List
6. V_id
- Event_hosts_id List(M)

4R:
1. Member_id
2. Group_id
3. Event_id
6. V_id

5T:
1. Group_id List
2. Member_id List

6V:
3. Event_id List
4. RSVP_id List
"""
