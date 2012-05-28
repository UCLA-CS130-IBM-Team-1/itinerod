$(document).ready(function() {
              
                  $( ".datepicker" ).datepicker();    //from jquery ui for date selection.. check out at a later time
                  
                  //Following code is for the auto-complete feature
                  var autocomplete = new google.maps.places.Autocomplete($("#address")[0], {});

                  google.maps.event.addListener(autocomplete, 'place_changed', function() {
                  var place = autocomplete.getPlace();
                  console.log(place.address_components);
                  });
                  
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
                                             +"\"end_time\":" + event_end_time+","
                                             +"\"itinerary\":" + itinerary +","
                                             +"\"location\":" +  event_location +","
                                             +"\"name\":"+ event_name +","
                                             +"\"start_time\":"+ event_start_time +","
                                             +"\"status\":"+ voting_status +","
                                             +"\"vote_deadline\":"+ voting_deadline 
                                             +"}" ;
                             alert(json_data);


                             $.ajax({
                             type:"POST",
                             url:"/api/itinerod/event/",
                             data: "{\"end_time\": \"2012-05-30T19:30:00\",\"itinerary\": \"/api/itinerod/itinerary/1/\", \"location\": \"Powell Library UCLA\", \"name\": \"IBM Team1 Meeting\", \"start_time\": \"2012-05-30T17:30:00\", \"status\": \"A\", \"vote_deadline\": null}",
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

	          var friendData; //TO DO: need to implement data to send of what users to delete from itinerary
	          $(".itinerary_friend_edit_button").click(function(){
	             $.ajax({
	             type:"PUT",
	             url:"/api/itinerod/itinerary/"+currentId+"/?format=json"+"&callback=?",
	             contextType: "application/json",
	             data: friendData,
	             dataType: 'json',
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
                                 contextType: "application/json"
                                      }).done(function(html) {

                                          var div_html = "";

                                          var events = html.events;
					  var users = html.users;
				          for(var i = 0, len = users.length; i < len; ++i)
					  {
						div_html += "<h2>Edit Friends</h2>";
                                                  div_html += "<div class='event_details'>";
						div_html += "<input type='checkbox' name='user1' value='"+ users[i].email +"'/> "+ users[i].email +"<br>";
                                                  div_html += "</div>";
					  }
                                          div_html += "<h2> Edit Itineraries </h2>" ;
                                          for(var i=0, len = events.length; i< len; ++i)
                                          {
                                          
                                                  div_html += "<div id="+events[i].id+">";
                                                  div_html += "<h3 class='event'>"+ events[i].name +"</h3>" ;
                                                  div_html += "Click Event to expand/contract edit details";
                                                  div_html += "<div class='event_details'>";
                                                  div_html += "Location: <input type='text' class='event_location' id="+events[i].location+" value= '"+ events[i].location +"'/>";
                                                  div_html +=  "</br>";
                                                  div_html += "Start Time: <input type='text' class='event_start_time' value= '"+ events[i].start_time +"'/>";
                                                  div_html +=  "</br>";
                                                  div_html += "End Time: <input type='text' class='event_end_time' value= '"+ events[i].end_time +"'/>";
                                                  div_html +=  "</br>";
                                                  div_html += "Voting Status: <input type='text' class='event_voting_status' value= '"+ events[i].status +"'/>";
                                                  div_html +=  "</br>";
                                                  div_html += "Voting Deadline: <input type='text' class='event_voting_deadline' value= '"+ events[i].vote_deadline +"'/>";
                                                  div_html +=  "</br>";
                                                  div_html += "Resource URI: <input type='text' class='resource_uri' value= '"+ events[i].resource_uri +"'/>";
                                                  div_html +=  "</br>";
                                                  div_html += "Resource URI: <input type='text' class='itinerary' value= '"+ events[i].itinerary +"'/>";
                                                  div_html += "</div>";
                                                  div_html += "<br />";
                                                  div_html += "<a class='event_edit_save' href='#'>SAVE</a>";
                                                  div_html += "</div>";
                                          }
                                          
                                          $("#editItinerary").html(div_html);
										  $('.addItinerary').hide();
                                          $('#editItinerary').show();

                                          hide_event_details();
                                      });

                  });

              });