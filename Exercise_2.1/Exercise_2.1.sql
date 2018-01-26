--SELECT MAX(Total) FROM Invoice

--SELECT MIN(Total) FROM Invoice

--SELECT BillingCity, COUNT(*) as Num FROM Invoice
	--GROUP BY BillingCity 
	--ORDER BY Num DESC
	
--SELECT COUNT(*) FROM Track
	--JOIN MediaType ON MediaType.MediaTypeId = Track.MediaTypeId
	--WHERE MediaType.Name = 'Protected AAC audio file'
	
--SELECT Artist.Name, COUNT(*) as Albums FROM Album
	--JOIN Artist ON Artist.ArtistId = Album.ArtistId
	--GROUP BY Album.ArtistId
	--ORDER BY Albums DESC
	
--SELECT Genre.Name, COUNT(*) as Tracks FROM Track
	--JOIN Genre ON Track.GenreId = Genre.GenreId
	--GROUP BY Track.GenreId
	--ORDER BY Tracks DESC
	
--SELECT FirstName, LastName, Total FROM Customer
	--JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
	--GROUP BY Total
	--ORDER BY Total DESC
	
SELECT Track.Name, InvoiceId FROM InvoiceLine
	JOIN Track ON Track.TrackId = InvoiceLine.TrackId
	

	