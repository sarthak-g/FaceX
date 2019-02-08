{% extends 'layout.html' %}

{% load static %}
{% block title %}Image Recognition | AI Course-work{% endblock %}
{% block content %}
<div id="particles-js"></div>
<div class="container" >
  <div class="col-lg-12" style="background: rgba(0,0,0,0.6);margin-top:3em;margin-bottom:5em;padding-top:1em;padding-bottom:3em;color:#fff;border-radius:10px;-webkit-box-shadow: 2px 2px 15px 0px rgba(0, 3, 0, 0.7);
-moz-box-shadow:    2px 2px 15px 0px rgba(0, 3, 0, 0.7);
box-shadow:         2px 2px 15px 0px rgba(0, 3, 0, 0.7);">
    <div class="col-lg-12">
      <a href="{% url 'logout' %}" class="text-right"><h5 ><i class="fa fa-user-circle" aria-hidden="true"></i> logout</a><br>
      <a href="{% url 'new_record' %}" class="text-right" style="float:right;"><h5 ><i class="fa fa-user-circle" aria-hidden="true"></i> New Record</a><br>
      <a href="{% url 'list_record' %}" class="text-right" style="float:right;"><h5 ><i class="fa fa-user-circle" aria-hidden="true"></i> All Record</a>
      <h1 class="text-center section-title" style="margin-bottom:2em">Smart Search with Face Recognition.</h1>
    </div>
    <style>
      h4{
        margin-bottom: 1.5em;
      }
      img{
        border-radius:50%;
        -webkit-transition: all 0.3s ease-in-out;
    -moz-transition: all 0.3s ease-in-out;
     transition: all 0.3s ease-in-out;
      }
      img:hover{
        -webkit-box-shadow: 2px 2px 21px 0px rgba(0, 3, 0, 0.91);
        -moz-box-shadow:    2px 2px 21px 0px rgba(0, 3, 0, 0.91);
        box-shadow:         2px 2px 21px 0px rgba(0, 3, 0, 0.91);
        border:2px solid #fff;
      }
      h3{
        margin-bottom: 1.3em;
      }
      a{
        color:inherit
      }
      a:hover{
        color:inherit;
        text-decoration: none;
      }
      .section-title:after {
        	content:' ';display:block;margin:0 auto;width:100px;margin-top: 6px;border:2px solid #d0d0d0;border-radius:4px;
        	-webkit-border-radius:4px;
        	-moz-border-radius:4px;
        	box-shadow:inset 0 1px 1px rgba(0, 0, 0, .05);
        	-webkit-box-shadow:inset 0 1px 1px rgba(0, 0, 0, .05);
        	-moz-box-shadow:inset 0 1px 1px rgba(0, 0, 0, .05);
          margin-bottom:1em;
        }
    </style>

    <div class="row">

      <div class="col-md-12">
        <h3 class="text-center">With OpenCV, LBPH</h3>
        <div class="col-md-4">
          <a href="/detect"><img src="{% static 'img/webcam.png' %}" class="img-responsive" /></a>
          <h4 class="text-center">Detect By Webcam</h4>
        </div>
        <div class="col-md-4">
          <a href="/trainer"><img src="{% static 'img/trainer.png' %}" class="img-responsive" /></a>
          <h4 class="text-center">Train The Classifier</h4>
        </div>
        <div class="col-md-4">
          <button type="button" style="background:transparent;border:none" data-toggle="modal" data-target="#myModal">
            <img src="{% static 'img/add.png' %}" class="img-responsive" />
          </button>
          <h4 class="text-center">Create Dataset</h4>
        </div>
      </div>
    </div>
</div><!-- Container -->




<!-- Modal -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="myModalLabel">Input unique id and wait for webcam</h4>
      </div>
      <div class="modal-body">
        <ul>
          <li>For higher accuracy, make sure to stay in room with good lightning.</li>
          <li>Please remove any type of accesories from face.</li>
          <li>Make sure your face in clearly visible in camera.</li>
          <li>Make sure your hair is not blocking the face.</li>
          <li>Make sure no other faces are within the cam frame.
        </ul>
        <hr/>
        <form action="/create_dataset" method="POST">
          {% csrf_token %}
          <div class="form-group">
            <label for="inputId">Enter Unique ID*</label>
            <input type="text" class="form-control" name="userId" id="inputId" placeholder="Enter Id">
          </div>
          <button type="submit" class="btn btn-warning">Submit</button>
        </form>
      </div>
    </div>
  </div>
</div>
</div>

{% endblock %}
