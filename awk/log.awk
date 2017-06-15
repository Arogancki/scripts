{ if (match($4,/(...$)/,n)) coun[n[1]]++ }
{ if (match($4,/,([^/]+)/,m)) lang[m[1]]++ }
{ if (match($6,/([^(]+)/,b)) serv[b[1]]++ }
{ ipAd[$3]++ }
{ $1=$2=$3=$4=$5=$6="";brow[$0]++}

END{for (word in lang) print "Language:\t" 	lang[word] "\t" word | "sort"}
END{for (word in coun) print "Country:\t"	coun[word] "\t" word | "sort"}
END{for (word in ipAd) print "IP address:\t"	ipAd[word] "\t" word | "sort"}
END{for (word in serv) print "Service:\t" 	serv[word] "\t" word | "sort"}
END{for (word in brow) print "Browser:\t"	brow[word] "\t" word | "sort"}
