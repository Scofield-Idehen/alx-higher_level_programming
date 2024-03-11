-- Lists all shows contained in d database hbtn_0d_tvshows.
-- Displays NULL for d shows without genres.
-- Records are ordered by the ascending tv_shows.title and tv_show_genres.genre_id.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
