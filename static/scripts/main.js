//console.log('hello');

/* jshint camelcase: false */
/* global define: false, _ */

//BACKBONE FUNCTIONS 

var AppRouter = Backbone.Router.extend({
	routes: {
		'':'home',
		'concierto': 'ver_concierto',
	}
});



var app_router = new AppRouter();
app_router.on('route:home', function(){
	console.log('home');
});
app_router.on('route:ver_concierto', function(){

});	


'use strict';
(function($){
	function floatLabel(inputType){
		$(inputType).each(function(){
			var $this = $(this);
			// on focus add cladd active to label
			$this.focus(function(){
				$this.next().addClass('active');
			});
			//on blur check field and remove class if needed
			$this.blur(function(){
				if($this.val() === '' || $this.val() === 'blank'){
					$this.next().removeClass();
				}
			});
		});
	}
	// just add a class of "floatLabel to the input field!"
	floatLabel('.floatLabel');
})(jQuery);


$('.show_modal').on('click', function(){

	var modal_to_show = $(this).data('modal');
	console.log(modal_to_show);
	$('.button_form').removeClass('active');
	$('.signin_form').hide();
	$('#entry_modal').animate({'height':'100%'}, function(){
		$('#entry_modal .container_entry_modal').animate({'top':'100px'});
		//$('.signin_form').removeClass('show');
		$('#'+modal_to_show+'_sign').show();

	});
	$('#button_'+modal_to_show).addClass('active');
	$('.close_modal').show();
});
$('.button_entry_modal').on('click','.button_form', function(){
	$('.button_form').removeClass('active');

	$(this).addClass('active');
	var modal_show  = $(this).data('modal');
	$('.signin_form').hide();
	$('#'+modal_show+'_sign').show();

});
$('.close_modal').on('click', function(){
	$('#entry_modal').animate({'height':'0px'}, function(){
		$('#entry_modal .container_entry_modal').css({'top':'-310px'});
		$('.signin_form').hide();
	});
	$('.close_modal').hide();
});