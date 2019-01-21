
jQuery(document).ready(function() {
	
    /*
        Fullscreen background
    */
    $.backstretch("https://i.imgur.com/AMf9X7E.jpg");
    
    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$.backstretch("resize");
    });
    
    /*
        Form
    */
    $('.registration-form fieldset:first-child').fadeIn('slow');
    
    $('.registration-form input[type="text"], .registration-form input[type="password"], .registration-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });

    var nexa = true;
    var lexa = true;

    var password = document.getElementById("form-password"),
            confirm_password = document.getElementById("form-repeat-password"),
            btn = document.getElementById("passbtn"),
            mail = document.getElementById("form-email")
            ;

        function validatePassword(){
           if(password.value != confirm_password.value) {
            //alert("Password Mismatch");
            confirm_password.setCustomValidity("Passwords Don't Match");
            nexa = false;
          } else {
            confirm_password.setCustomValidity('');
            nexa = true;
          }
        }

        function isitEmail() {
            var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
             var temp = regex.test(mail.value);
             console.log('called',temp );
             lexa = temp;
             console.log(nexa,lexa)
        }



    btn.onclick = isitEmail;
    mail.onchange = isitEmail;
    mail.onkeyup = isitEmail;

    btn.onclick = validatePassword;
    password.onchange = validatePassword;
    confirm_password.onkeyup = validatePassword;
    
    // next step
    $('.registration-form .btn-next').on('click', function() {
    	var parent_fieldset = $(this).parents('fieldset');
    	var next_step = true;
    	
    	parent_fieldset.find('input[type="text"], input[type="password"], textarea').each(function() {
    		if( $(this).val() == "" || nexa == false || lexa == false) {
    			$(this).addClass('input-error');
    			next_step = false;
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});

    	if( next_step ) {
    		parent_fieldset.fadeOut(400, function() {
	    		$(this).next().fadeIn();
	    	});
    	}
    	
    });
    
    // previous step
    $('.registration-form .btn-previous').on('click', function() {
    	$(this).parents('fieldset').fadeOut(400, function() {
    		$(this).prev().fadeIn();
    	});
    });
    
    // submit
    $('.registration-form').on('submit', function(e) {
    	
    	$(this).find('input[type="text"], input[type="password"], textarea').each(function() {
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});
    	
    });
    
    
});
