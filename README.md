# Maze
Virtual rendition of Maze created by Christopher Manson

The objectives of the Maze is to head to room 45 and then return to the start in the least amount of steps.
The maze may contain clues or lies throughout the description and visual pages.

Taking pictures and data values from the pages of book and storing them locally.

The maze is generated and run off a local Flask app with the map locations generated from the pull requests
made from redirections on the html pages. The amount of pages is only 45 and the description was then pulled from
images and parsed using pytesseract.

Alternative option is to build the maze with individual pages and have them displayed using a link. However, this will run
off a web server without the need for many html locations.