$(document).ready(function() {

                  function set_datepicker(){
                  $(".event_start_time").datepick();
                  }
                  $("#datepicker_example").datepick();
                  /*
                   //Pralav - from jquery ui for date selection.. check out at a later time
                  function set_datepicker(){
                  $(function() {
		  $( ".datepicker" ).datepicker();
	          });
	          }                     */

                  //Following code is for the auto-complete feature
                  var autocomplete = new google.maps.places.Autocomplete($("#address")[0], {});

                  google.maps.event.addListener(autocomplete, 'place_changed', function() {
                  var place = autocomplete.getPlace();
                  console.log(place.address_components);
                  });
                  
                  function set_autocomplete(){
                      var address_autocomplete = new google.maps.places.Autocomplete($("#add_event_location")[0], {});
                      google.maps.event.addListener(address_autocomplete, 'place_changed', function() {
                      var place = autocomplete.getPlace();
                      console.log(place.address_components);
                  });
                  }
                  
                   //Expansion/contraction of div related code
                  $(".event").live('click',function(){
                           $(this).next().slideToggle('slow');
                           });
                  function hide_event_details()
                  {
                           $(".event_details").hide();
                  }
                  //Save button clicks in edit event details tab
                  $(".event_edit_save").live('click',function(){
                             var event_id = $(this).parent().attr("id");
                             var event_name = $(this).parent().children(".event").html();
                             var event_start_time = $(this).parent().children(".event_details").find(".event_start_time").val();
                             var event_end_time = $(this).parent().children(".event_details").find(".event_end_time").val();
                             var voting_status =  $(this).parent().children(".event_details").find(".event_voting_status").val();
                             var voting_deadline = $(this).parent().children(".event_details").find(".event_voting_deadline").val();
                             var resource_uri = $(this).parent().children(".event_details").find(".resource_uri").val();
                             var itinerary = $(this).parent().children(".event_details").find(".itinerary").val();
                             var event_location = $(this).parent().children(".event_details").find(".event_location").val();
                             
                             //Create input for the AJAX call
                             
                             var json_data = "{" + ""
                                             +"\"end_time\":\"" + event_end_time+"\","
                                             +"\"itinerary\":\"" + itinerary +"\","
                                             +"\"location\":\"" +  event_location +"\","
                                             +"\"name\":\""+ event_name +"\","
                                             +"\"start_time\":\""+ event_start_time +"\","
                                             +"\"status\":\""+ voting_status +"\","
                                             +"\"vote_deadline\":\""+ voting_deadline+"\""
                                             +"}" ;
                             alert(json_data);

                             var hard_coded_data="{\"end_time\": \"2012-05-30T19:30:00\",\"itinerary\": \"/api/itinerod/itinerary/1/\", \"location\": \"Powell Library UCLA\", \"name\": \"IBM Team1 Meeting\", \"start_time\": \"2012-05-30T17:30:00\", \"status\": \"A\", \"vote_deadline\": null}";

                             $.ajax({
                             type:"PUT",
                             url:"/api/itinerod/event/"+event_id+"/",
                             data: json_data,
                             dataType: 'application/json',
                             contentType: 'application/json',
                             }).done(function(html){
                                      alert("done");
                             });

                             /*
                             $.ajax({
                             type:"PATCH",
                             url:"http://localhost:8000/api/itinerod/event/54/", // THIS ID IS SPECIFIC TO PRESTON's DB
                             data: "{\"end_time\": \"2012-06-06T19:30:00\", \"start_time\": \"2012-06-06T17:30:00\"}",
                             dataType: 'application/json',
                             contentType: 'application/json',
                             }).done(function(html){
                                      alert("done");
                             });
                             */
                             
                             /*
                             $.ajax({
                             type:"DELETE",
                             url:"http://localhost:8000/api/itinerod/event/54/",
                             dataType: 'application/json',
                             contentType: 'application/json',
                             }).done(function(html){
                                      alert("done");
                             });
                             */
                   });

                   //Code to handle add event clicks on edit/add events page
                   $(".event_add").live('click',function(){

                      var event_itinerary = $("#add_event_itinerary").val();
                      var event_name = $("#add_event_name").val();
                      var event_location = $("#add_event_location").val();
                      var event_start_time = $("#add_event_start_time").val();
                      var event_end_time = $("#add_event_end_time").val();
                      var event_voting_deadline = $("#add_event_voting_deadline").val();
                      var event_voting_status = $("#add_event_voting_status").val();
                      
                      alert(event_name+event_itinerary+event_location+event_start_time+event_end_time+event_voting_deadline);
                      
                      var json_data = "{" + ""
                                      +"\"end_time\":\"" + event_end_time+"\","
                                      +"\"itinerary\":\"" + event_itinerary +"\","
                                      +"\"location\":\"" +  event_location +"\","
                                      +"\"name\":\""+ event_name +"\","
                                      +"\"start_time\":\""+ event_start_time +"\","
                                      +"\"status\":\""+ event_voting_status +"\","
                                      +"\"vote_deadline\":\""+ event_voting_deadline+"\""
                                      +"}" ;
                     alert(json_data);

                      $.ajax({
                             type:"POST",
                             url:"/api/itinerod/event/?format=json",
                             data: json_data,
                             dataType: 'application/json',
                             contentType: 'application/json',
                             }).done(function(html){
                                      alert("done");
                                      location.reload();
                      });

                   });

	          $(".itinerary_friend_edit_button").live('click',function(){
                     var currentId = $(this).attr('id');
		     var friend = "";
		     var users = $("#users").val();
		     var usersParsed = JSON.parse(users);
		     if($('#friendCheck').attr('checked'))
			friend = $("#friendCheck").val();
			alert(friend);
		     for(var i = 0; i < usersParsed.length; i++){
			if(usersParsed[i].email == friend){
				usersParsed[i] = null;
			}
		     }
		     users = "{" + "\"users\":" + JSON.stringify(usersParsed) + "}";
			  var hard_code = "{"+"\"users\": [{\"email\": \"stefanwoj89@ucla.edu\", \"first_name\": \"\", \"itineraries\": [\"/api/itinerod/itinerary/10/\"], \"last_name\": \"\", \"resource_uri\": \"/api/itinerod/user/2/\", \"username\": \"stefanwoj89\"}]}";

var hard_code2 = "{"+"\"users\": [{\"email\": \"guiltyspark7750@gmail.com\", \"first_name\": \"\", \"itineraries\": [\"/api/itinerod/itinerary/1/\", \"/api/itinerod/itinerary/2/\", \"/api/itinerod/itinerary/3/\", \"/api/itinerod/itinerary/4/\", \"/api/itinerod/itinerary/5/\", \"/api/itinerod/itinerary/6/\", \"/api/itinerod/itinerary/7/\", \"/api/itinerod/itinerary/8/\", \"/api/itinerod/itinerary/9/\"], \"last_name\": \"\", \"resource_uri\": \"/api/itinerod/user/1/\", \"username\": \"guiltyspark7750@gmail.com\"}]}";
		     alert(hard_code2);
	             $.ajax({
	             type:"PATCH",
	             url:"/api/itinerod/itinerary/"+currentId+"/",
	             contentType: "application/json",
	             data: hard_code2,
	             dataType: 'application/json',
                     })
	          })


			// "Add" button binding
			$('#newItinerary').click(function(){
				$('#editItinerary').hide();
				$('.addItinerary').show();
				
				// Remove styling of selected edit buttons
          		$('li.selected').removeClass('selected');

			});
			
			// "Edit" button binding
                  $(".itinerary_edit_button").click(function(){
                  		// Change style of button
                  		$('li.selected').removeClass('selected');
                  		$(this).parent().addClass('selected');
                  
                                 var currentId = $(this).attr('id');
                                // alert("Hi");
                                 $.ajax({
                                 type:"GET",
                                 url: "/api/itinerod/itinerary/"+currentId+"/?format=json"+"&callback=?",
                                 contentType: "application/json"
                                      }).done(function(html) {

                                          var div_html = "";

                                          var events = html.events;
					  var users = html.users;
						div_html += "<h2>Remove your Friends below</h2>";
                                                  div_html += "<div class='event_friends'>";
				          for(var i = 0, len = users.length; i < len; ++i)
					  {
						var name = "user"+i;
						div_html += users[i].email + "<br>";
                                                div_html += "<a class='' id ='' href='/api/delete_friend/"+currentId+"/"+users[i].id+"'> Remove Friend </a>";
					  }
						
                                                  div_html += "</div>";
					  
					  //Before listing the events, get the itinerary to which the events belong
					  //Used in the "add" event function
					  var itinerary_identifier = "/api/itinerod/itinerary/"+currentId+"/";
					  /*if(events.length>0)
                                          {
                                            itinerary_identifier = events[0].itinerary;
                                          }
					  else*/
						//itinerary_identifier = "/api/itinerod/itinerary/"+currentId+"/"; // this is a much better version. What if itinerary is empty of events?
                                          div_html += "<h2> Edit Your Events below </h2>" ;   
                                          div_html += "Click Event to expand/contract edit details";

                                          div_html += getHTMLforEditButtonClick(events,itinerary_identifier)
                                          
                                          $("#editItinerary").html(div_html);
					  $('.addItinerary').hide();
                                          $('#editItinerary').show();


                                          hide_event_details();
                                          set_datepicker();
                                          set_autocomplete();
                                      });

                  });
                  
                  function getHTMLforEditButtonClick(events,itinerary_identifier)
                  {           var div_html = "";
                              var month_select = "<select name='start_date_month' class='month_selector'>"+
                                                 "<option value='0'>---</option>"+
                                                 "<option value='1'>January</option>"+
                                                 "<option value='2'>February</option>"+
                                                 "<option value='3'>March</option>"+
                                                 "<option value='4'>April</option>"+
                                                 "<option value='5'>May</option>"+
                                                 "<option value='6'>June</option>"+
                                                 "<option value='7'>July</option>"+
                                                 "<option value='8'>August</option>"+
                                                 "<option value='9'>September</option>"+
                                                 "<option value='10'>October</option>"+
                                                 "<option value='11'>November</option>"+
                                                 "<option value='12'>December</option>"+
                                                 "</select>";
                              for(var i=0, len = events.length; i< len; ++i)
                                          {
                                                   var start_date_time = events[i].start_time;
                                                   var start_month =  start_date_time.substring(5,7);
                                                   var start_day =   start_date_time.substring(8,10);
                                                   var start_year =   start_date_time.substring(0,4);
                                                   var start_time =   start_date_time.substring(11,19);
                                                   
                                                   var end_date_time = events[i].end_time;
                                                   var end_month =  end_date_time.substring(5,7);
                                                   var end_day =   end_date_time.substring(8,10);
                                                   var end_year =   end_date_time.substring(0,4);
                                                   var end_time =   end_date_time.substring(11,19);

                                                   
                                                   var start_date = start_month + "/" + start_day + "/" + start_year;
                                                   var end_date = end_month + "/" + end_day + "/" + end_year;

                                                  div_html += "<div id="+events[i].id+" style='border-bottom:solid;'>";
                                                  div_html += "<h3 class='event'>"+ events[i].name +"</h3>" ;
                                                  div_html += "<div class='event_details' style='display: block;'>";

                                                  div_html += "<label class='fancyLabel textLabel' for='"+events[i].id+"_location'>Location: </label>";
                                                  div_html += "<input type='text' class='event_location' id="+events[i].id+"_location' value= '"+ events[i].location +"'/>";
                                                  div_html +=  "</br>";

                                                  div_html += "<label class='fancyLabel textLabel' for='"+events[i].id+"_start_time'>Start Time: </label>";
                                                  div_html += "<input type='text' class='event_start_time' id="+events[i].id+"_start_time' value= '"+ start_date +"'/>";
                                                  div_html +=  "</br>";

                                                  div_html += "<label class='fancyLabel textLabel' for='"+events[i].id+"_end_time'>End Time: </label>";
                                                  div_html += "<input type='text' class='event_end_time' id="+events[i].id+"_end_time' value= '"+ end_date +"'/>";
                                                  div_html +=  "</br>";

                                                  div_html += "<label class='fancyLabel textLabel' for='"+events[i].id+"_voting_status'>Vote: </label>";
                                                  div_html += "<input type='text' class='event_voting_status' id="+events[i].id+"_voting_status' value= '"+ events[i].status +"'/>";
                                                  div_html +=  "</br>";

                                                  div_html += "<label class='fancyLabel textLabel' for='"+events[i].id+"_voting_deadline'>Deadline: </label>";
                                                  div_html += "<input type='text' class='event_voting_deadline' id="+events[i].id+"_voting_deadline' value= '"+ events[i].vote_deadline +"'/>";
                                                  div_html +=  "</br>";

                                                  div_html += "<input type='hidden' class='resource_uri' id="+events[i].id+"_resource_uri' value= '"+ events[i].resource_uri +"'/>";
                                                  div_html +=  "</br>";

                                                  div_html += "<input type='hidden' class='itinerary' id="+events[i].id+"_itinerary' value= '"+ events[i].itinerary +"'/>";
                                                  div_html += "</div>";
                                                  div_html += "<br />";
                                                  div_html += "<a class='event_edit_save' href='#'>Save Changes</a>";
                                                  div_html += "<br />";
                                                  div_html += "<a class='event_delete' href='#'>Delete</a>";
                                                  div_html += "<input type='hidden' class='datepicker' size='30' />";
                                                  div_html += "</div>";
                                          }

                                          //adding div to add itinerary
                                          div_html += "<div class='add_event'>";
                                          div_html += "<h2>Add an Event to the Itinerary</h2>";
                                          div_html += "<label class='fancyLabel textLabel' for='add_event_name'>Event: </label>";
                                          div_html += "<input id='add_event_name' type='text' /> <br />";
                                          div_html += "<label class='fancyLabel textLabel' for='add_event_location'>Location: </label>";
                                          div_html += "<input id = 'add_event_location' type='text' /> <br />";
                                          div_html += "<label class='fancyLabel textLabel' for='add_event_start_time'>Start Time: </label>";
                                          div_html += "<input id = 'add_event_start_time' type='text' /> <br />";
                                          div_html += "<label class='fancyLabel textLabel' for='add_event_end_time'>End Time: </label>";
                                          div_html += "<input id = 'add_event_end_time' type='text' /> <br />";
                                          div_html += "<label class='fancyLabel textLabel' for='add_event_voting_deadline'>Voting Deadline: </label>";
                                          div_html += "<input id='add_event_voting_deadline' type='text' /> <br />";
                                          div_html += "<input type='text' class='datepicker' /> <br />";
                                          div_html += "<input id='add_event_itinerary' type='hidden' value='"+ itinerary_identifier + "'/><br />";
                                          div_html += "<input id='add_event_voting_status' type='hidden' value='V'/><br />";
                                          div_html += "<a class='event_add' href='#'> Add Event </a>";
                                          div_html += "</div>";
                                          
                                          return div_html;
                  }
                  

                  //code to remove events from the page
                  $(".event_delete").live('click', function(){
                             var resource_uri = $(this).parent().children(".event_details").find(".resource_uri").val();

                             $(this).parent().remove();
                             //add an ajax call to remove the itinerary
                             $.ajax({
                               type:'DELETE',
                               url:resource_uri
                             }).done(function(){
                               alert("The event has been deleted");
                             });
                    });

              });
