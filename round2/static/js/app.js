/**
 * Created by root on 1/2/15.
 */
function settimer(starttime)
{
    var e=1;
    var d=starttime.split(' ')[0].split('-');
    var t=starttime.split(' ')[1].split('+')[0].split(':');
    var yyyy =d[0];
    var mm =d[1]-1;
    var dd =d[2];
    var hr =t[0];
    var min =t[1];
    var s=t[2];
	var start = new Date(Date.UTC(yyyy,mm,dd,hr, min,s));
    console.log(start);
    var end= new Date(start-((-1*e)*60000));
    console.log(end);
	$('.yolo').countdown({until: end, format: 'HMS',expiryUrl: '/end/'});
}

var x;
$( ".solvebtn" ).hover(
function() {
x=$(this).html();
$(this).removeClass('btn-danger')
$(this).addClass('btn-info');
$( this ).html("Solve Again?");
}, function() {
$(this).removeClass('btn-info')
$(this).addClass('btn-danger');
$( this ).html(x);
}
);