CREATE TABLE "Vinyl" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"image" varchar(100) NULL,
	"artist" varchar(100) NOT NULL,
	"name" varchar(100) NOT NULL,
	"price" integer NOT NULL,
	"saved" bool NOT NULL DEFAULT 0,
	"sold" bool NOT NULL DEFAULT 0,
	"info" text NOT NULL DEFAULT ""
);

INSERT INTO "Vinyl" (artist, name, price) VALUES ('Edge of Sanity','Crimson',27500);