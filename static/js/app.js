function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

function enroll(course_id){
   $.ajax({  
          type: "POST",
          url: ENROLL,
          data: {"id": course_id},
          dataType: "json",
          headers: {"X-HTTP-Method-Override": "POST", "X-CSRFToken": getCookie("csrftoken")},
          // beforeSend: function(){$(".loader").show()},
          success: function(res) {
            console.log(res.success)
            if(res.success){
              $('#stc-'+course_id).html(res.data.count);
              $('#av-'+course_id).html(res.data.available);
              $('#enroll-'+course_id).remove();
              $('#td-'+course_id).html('<a id="quit-'+course_id+'" href="javascript:void(0)" onclick="quit('+course_id+')" class="enroll-btn btn btn-xs btn-danger">Quit</a>');
            } else {
              alert(res.message)
            }
          },
          error: function(res){
            alert(res.responseJSON.message)
            // console.log(res.responseText)
            // $.toaster({ priority : 'danger', title : 'Error!', message : 'Body can not be empty.'});
          }
      }).done(function(){$(".loader").hide()});
}

function quit(course_id){
   $.ajax({  
          type: "POST",
          url: QUIT,
          data: {"id": course_id},
          dataType: "json",
          headers: {"X-HTTP-Method-Override": "POST", "X-CSRFToken": getCookie("csrftoken")},
          // beforeSend: function(){$(".loader").show()},
          success: function(res) {
            console.log(res.success)
            if(res.success){
              $('#stc-'+course_id).html(res.data.count);
              $('#av-'+course_id).html(res.data.available);
              $('#quit-'+course_id).remove()
              $('#td-'+course_id).html('<a id="enroll-'+course_id+'" href="javascript:void(0)" onclick="enroll('+course_id+')" class="enroll-btn btn btn-xs btn-info">Enroll Now!</a>')
            } else {
              alert(res.message)
            }
          },
          error: function(res){
            alert(res.responseJSON.message)
          }
      }).done(function(){$(".loader").hide()});
}