-- Slideshow (Slide 26)- Using LEFT and RIGHT functions
SELECT VendorContactFName, VendorContactLName,
	LEFT(VendorContactFName,1)+
	LEFT(VendorContactLName,2) AS Initials
FROM vendors;