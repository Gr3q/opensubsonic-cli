# Inconsistencies

* `ItemDate` description and spec doesn't match (in required fields)
* Disc number must be a number but obviously it can be other things
* `getAlbumInfo2` return type incorrect (based on `AlbumList`)?
* `downloadPodcastEpisode` return type incorrect?
* `deleteBookmark` summary and description is wrong
* `download` error payload schema incomplete
* `getArtists` page first `artists` link is broken
* `getAvatar` `username` parameter is "required" and has a "default" as well. 

## Future Improvements

* Could use inheritance for ArtistInfo and ArtistInfo2
