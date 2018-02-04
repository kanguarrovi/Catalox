CREATE TABLE "Vinyl" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"image" varchar(100) NULL,
	"artist" varchar(100) NOT NULL,
	"name" varchar(100) NOT NULL,
	"price" real NOT NULL,
	"status" varchar(100) NOT NULL,
	"info" text NOT NULL DEFAULT ""
);

INSERT INTO "Vinyl" (artist, name, price, status) VALUES ('Edge of Sanity', 'Crimson', 49.95, 'ava');