SELECT users.first_name, users.last_name, user2.first_name AS friend_first, user2.last_name AS friend_last
FROM users
JOIN friendships ON friendships.user_id = users.id
	JOIN users AS user2 ON user2.id = friendships.friend_id
ORDER BY user2.last_name ASC