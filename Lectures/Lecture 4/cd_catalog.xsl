<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
<head>
	<link rel="stylesheet" href="style.css" />
</head>
<body>
<div class="container">
<table>
	<tr>
		<th>Title</th>
		<th>Artist</th>
		<th>Country</th>
		<th>Company</th>
		<th>Price</th>
		<th>Year</th>
	</tr>
	<xsl:for-each select="CATALOG/CD">
	<tr>
		<td><xsl:value-of select="TITLE" /></td>
		<td><xsl:value-of select="ARTIST" /></td>
		<td><xsl:value-of select="COUNTRY" /></td>
		<td><xsl:value-of select="COMPANY" /></td>
		<td><xsl:value-of select="PRICE" /></td>
		<td><xsl:value-of select="YEAR" /></td>
	</tr>
	</xsl:for-each>
</table>
</div>
</body>
</html>
</xsl:template>
</xsl:stylesheet>