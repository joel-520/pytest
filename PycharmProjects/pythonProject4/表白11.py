520
*{margin: 0; padding: 0;}

ul,ol{list-style: none;}

a{text-decoration: none;color: inherit;}

.clearfix:after{content: '';display: block;clear: both;}

.clear{clear: both;}

body{
background-color: #8a0a0a;

}

.love{
display: table;

flex-wrap: wrap;

margin: 100px auto;

}

.box{
float:left;

width: 25px;

height: 25px;

border-radius: 2px;

margin-right: 2px;

margin-bottom: 2px

}

.box:hover{
background: #8a0a0a;

}

.box:not(.transparent){
background-color: #fff;

opacity: 0;

transform: translateY(-300px);

animation: move 4s infinite;

}

@keyframes move{
25%{
opacity: 1;

transform: translateY(0);

}

50%{
opacity: 1;

transform: translateY(0);

}

65%{
opacity: 1;

transform: translateY(0);

}

100%{
opacity: 0;

transform: translateY(300px);

}

}

.box.delay1{
animation-delay: .1s;

}

.box.delay2{
animation-delay: .2s;

}

.box.delay3{
animation-delay: .4s;

}

.box.delay4{
animation-delay: .5s;

}

.box.delay5{
animation-delay: .7s;

}

.box.delay6{
animation-delay: .9s;

}

p{
width: 1000px;

margin: 200px auto 0;

color: #fff;

font-size: 40px;

text-align: center;

}