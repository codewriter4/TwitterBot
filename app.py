console.log('my twitter bot is running')
var Twit = require('twit');

var config= require('./config');
var T = new Twit(config);

var schedule = require('node-schedule');
var rule = new schedule.RecurrenceRule();
rule.minute = 0; //on the hour
var rule2 = new schedule.RecurrenceRule();
rule2.hour=[8,12,16,20]; //at noon
var rule3 = new schedule.RecurrenceRule();


var hours = schedule.scheduleJob(rule, function(){
tweetIt();
});

var week= new schedule.RecurrenceRule();
week.dayofWeek=[1,3,5,0];
week.hour=[14];
var day = schedule.scheduleJob(week, function(){
  reTweet2();
  mylikeIT();
});

var week= new schedule.RecurrenceRule();
week.dayofWeek=[2,4,6,0];
week.hour=[10];
var day = schedule.scheduleJob(week, function(){
  reTweet();
  mylikeIT();
});

function tweetIt(){
    var d = Date()
    var tweet={
        status: ///enter your tweet message here in quotes
    }
    T.post('statuses/update',tweet, tweeted);
    function tweeted(err,data,response){
        if(err){
            console.log('something went wrong:'+d)
            console.log(err)
        }else{
            console.log('it worked! '+d)
        }
    }

}

function likeIT(){
        T.get('statuses/home_timeline',
    function(err,data,response){
        for(var i =0; i<data.length; i++){
            T.post('favorites/create',{id:data[i]['id_str']})
    }

    })
}



function mylikeIT(){
         T.get('statuses/user_timeline',
        {screen_name:'nameoftwitteraccountyouwanttolike',count:10},
    function(err,data,response){
        for(var i =0; i<data.length; i++){
            T.post('favorites/create',{id:data[i]['id_str']})
    }

    })
}

function reTweet(){
    T.get('statuses/user_timeline',
        {screen_name:'nameoftwitteraccountyouwanttoretweet',count:1},
    function(err,data,response){
        for(var i =0; i<data.length; i++){
            T.post('statuses/retweet/:id',{id:data[i]['id_str']})
    }

    })
   }

function reTweet2(){
    T.get('statuses/user_timeline',
        {screen_name:'nameoftwitteraccountyouwanttoretweet',count:1},

    function(err,data,response){
        for(var i =0; i<data.length; i++){
            T.post('statuses/retweet/:id',{id:data[i]['id_str']})
    }

    })
   }
