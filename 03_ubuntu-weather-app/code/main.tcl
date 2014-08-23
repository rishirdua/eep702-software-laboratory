#!/usr/bin/wish

#the main GUI

#global variables
set pythonctl "/usr/bin/python"
global pythonctl
global allcities
global allwoeids
global woeidval

#calls a python code that fetches records of last n days and shows it to the user
proc showpast {} {
	global pythonctl
	set num_of_days [.fr.scl_days get]
	set woeid [.fr.ent_woeid get]
	exec $pythonctl writepastweather.py $woeid $num_of_days > buffer.txt
	set fp [open "buffer.txt" r]
	set file_data [read $fp]
	close $fp
	set data [split $file_data "\n"]
	foreach line $data {
	     puts $line
	}
	.fr.lbl_weather configure -text $file_data
	return $line
}

#calls a python code that searches Yahoo API and adds records of next n days to the database, after that calls a python code that fetches records of next n days and shows it to the user
proc showfuture {} {
	global pythonctl
	set num_of_days [.fr.scl_days get]
	set woeid [.fr.ent_woeid get]
	exec $pythonctl getweather.py $woeid
	exec $pythonctl writefutureweather.py $woeid $num_of_days > buffer.txt
	set fp [open "buffer.txt" r]
	set file_data [read $fp]
	close $fp
	set data [split $file_data "\n"]
	foreach line $data {
	     puts $line
	}
	.fr.lbl_weather configure -text $file_data
	return $line
}

#searches for woeid by cordinate
proc searchcordi {} {
	global pythonctl
	global allcities
	global allwoeids
	set lat [.fr.ent_lat get]
	set long [.fr.ent_long get]
	exec $pythonctl woeidfromcordi.py $lat $long
	set fp [open "woeids.txt" r]
	set file_data [read $fp]
	close $fp
	set data [split $file_data "\n"]
	set allwoeids $data
	
	set fp [open "cities.txt" r]
	set file_data [read $fp]
	close $fp
	set data [split $file_data "\n"]
	set allcities $data
}

#searches for woeid by name of the city (query string)
proc searchcities {} {
	global pythonctl
	global allcities
	global allwoeids
	set searchstring [.fr.ent_query get]
	exec $pythonctl woeidfromquery.py $searchstring
	set fp [open "woeids.txt" r]
	set file_data [read $fp]
	close $fp
	set data [split $file_data "\n"]
	set allwoeids $data
	
	set fp [open "cities.txt" r]
	set file_data [read $fp]
	close $fp
	set data [split $file_data "\n"]
	set allcities $data
}

#updates woeid whenever user makes a selection
proc setLabel { idx } {
global woeidval
	set val [.fr.lb_woeids get $idx]
	#.fr.ent_woeid configure -text $val
	puts $val	
	set woeidval $val
}

#updates woeid whenever user makes a selection
proc setLabel2 { idx } {
global woeidval
	set val [.fr.lb_woeids get $idx]
	#.fr.ent_woeid configure -text $val
	puts $val	
	set woeidval $val
}

#builds the main GUI
proc screen {} {
	
	frame .fr -padx 5 -pady 5
	pack .fr -fill both -expand 1

	ttk::style configure TButton -width 8 -height 8 -font "serif 10" 
	
	#row 0
	label .fr.lbl_query -text "Search by City"
	grid .fr.lbl_query -row 0 -column 0 -columnspan 2
	entry .fr.ent_query 
	grid .fr.ent_query -row 0 -column 2 -columnspan 4
	ttk::button .fr.ttk_scity -text "Search" -command searchcities
	grid .fr.ttk_scity -row 0 -column 6 -columnspan 2

	#row 1
	label .fr.lbl_cordi -text "Search by Cordinates"
	grid .fr.lbl_cordi -row 1 -column 0 -columnspan 2
	label .fr.lbl_lat -text "Lat"
	grid .fr.lbl_lat -row 1 -column 2 -columnspan 1
	entry .fr.ent_lat -width 5
	grid .fr.ent_lat -row 1 -column 3 -columnspan 1
	label .fr.lbl_long -text "Long"
	grid .fr.lbl_long -row 1 -column 4 -columnspan 1
	entry .fr.ent_long -width 5
	grid .fr.ent_long -row 1 -column 5 -columnspan 1
	ttk::button .fr.ttk_scordi -text "Search" -command searchcordi
	grid .fr.ttk_scordi -row 1 -column 6 -columnspan 2
	
	#row 2,3,4
	listbox .fr.lb_woeids -listvariable allwoeids
	bind .fr.lb_woeids <<ListboxSelect>> { setLabel [%W curselection]}
	#grid .fr.lb_woeids -row 2 -column 0 -rowspan 3 -columnspan 8
	listbox .fr.lb_cities -listvariable allcities
	bind .fr.lb_cities <<ListboxSelect>> { setLabel2 [%W curselection]}
	grid .fr.lb_cities -row 2 -column 0 -rowspan 3 -columnspan 8 -sticky ew

	#row 5
	label .fr.lbl_woeid -text "Woeid"
	grid .fr.lbl_woeid -row 5 -column 0 -columnspan 2
	entry .fr.ent_woeid -textvariable woeidval
	grid .fr.ent_woeid -row 5 -column 2 -columnspan 2
	label .fr.lbl_days -text "Num of days"
	grid .fr.lbl_days -row 5 -column 4 -columnspan 2
	scale .fr.scl_days -orient horizontal -from 0 -to 25  -variable numofdays -showvalue true
	grid .fr.scl_days -row 5 -column 6 -columnspan 2
	
	#row 6
	ttk::button .fr.ttk_past -text "Check weather history" -command showpast -width 25
	grid .fr.ttk_past -row 6 -column 0 -columnspan 4
	ttk::button .fr.ttk_future -text "Check weather prediction" -command showfuture -width 25
	grid .fr.ttk_future -row 6 -column 4 -columnspan 4

	#row 7,8,9,10
	label .fr.lbl_weather -text ""
	grid .fr.lbl_weather -row 7 -column 0 -rowspan 8 -columnspan 4 -sticky news


	grid columnconfigure .fr 0 -pad 3
	grid columnconfigure .fr 1 -pad 3
	grid columnconfigure .fr 2 -pad 3
	grid columnconfigure .fr 3 -pad 3
	grid columnconfigure .fr 4 -pad 3
	grid columnconfigure .fr 5 -pad 3
	grid columnconfigure .fr 6 -pad 3
	grid columnconfigure .fr 7 -pad 3

	grid rowconfigure .fr 0 -pad 3        
	grid rowconfigure .fr 1 -pad 3  
	grid rowconfigure .fr 2 -pad 3  
	grid rowconfigure .fr 3 -pad 3  
	grid rowconfigure .fr 4 -pad 3
	grid rowconfigure .fr 5 -pad 3  
	grid rowconfigure .fr 6 -pad 3  
	grid rowconfigure .fr 7 -pad 3  
	grid rowconfigure .fr 8 -pad 3  
	grid rowconfigure .fr 4 -pad 3
	grid rowconfigure .fr 10 -pad 3    


	wm title . "Weather App" 
	#wm geometry . +300+300
}

#call the main function
screen
