// odoo.define('education', function (require) {
//     var core = require('web.core');
//     alert(core._t('This is a test notification'));
//     return {}
//  });

console.log('test javascript!!!')

// $(document).ready(function() {
//     function fetchCourses() {
//         // Define the URL of the API endpoint
//         var apiUrl = '/api/courses';
    
//         // AJAX call to fetch tasks data
//         $.ajax({
//             url: apiUrl,
//             type: 'GET',
//             dataType: 'json',
//             success: function(response) {
//                 if (response.status === 'success') {
//                     var coursesData = response.data;
//                     var courseListDiv = $('#course-list');
    
//                     // Loop through the task data and render it
//                     for (var i = 0; i < coursesData.length; i++) {
//                         var course = coursesData[i];
//                         var courseHtml = `
//                             <div class="col-sm-3">
//                                 <div class="card m-3" style="width: 18rem;">
//                                     <div class="card-img-top img-content">
//                                         <img  src="${course.image_url}"
//                                             class="w-100 image-main" alt="image"/>
//                                     </div>
                                
//                                     <div class="card-body" id="card_body">
//                                         <h3 class="card-title">${course.name}</h3>
//                                         <div class = "mt-1" id="tags">
//                                         <p class="badge bg-danger">${course.type_of_course}</p>
//                                         <p class="badge badge-success">${course.level_of_course}</p>
//                                     </div>
//                                         <p class="card-text">With ${course.number_of_lesson} lessons</p>
//                                         <a href="/course/${course.id}" class="btn btn-primary">
//                                             Start learning
//                                         </a>
//                                     </div>
//                                 </div>
//                             </div>
//                         `;
//                         courseListDiv.append(courseHtml);
//                     }
//                 }
//             },
//             error: function(error) {
//                 console.error('Error fetching tasks:', error);
//             }
//         });
//     }



//     function fetchCourseDetail(courseId) {
//         var courseDetailUrl = `/api/course/${courseId}`;
//         console.log(courseId);

//         $.ajax({
//             url: courseDetailUrl,
//             type: 'GET',
//             dataType: 'json',
//             success: function(response) {
//                 if (response.status === 'success') {
//                     var course = response.data;
//                     var courseDetailDiv = $('#course-detail-container');

//                     var courseHtml = `
//                             <section class="pt32 pb32 bg-secondary oe_custom_bg">
//                                 <div class="container text-center">
//                                     <h1 class="text-light">${course.name}</h1>
//                                     <a href="#" class="btn btn-primary mt-1"
//                                         style="box-shadow: 2px 2px 0px 0px rgba(255,255,255,1);
//                                         width: 5rem;">
//                                         Start
//                                     </a>
//                                 </div>
//                             </section>
//                             <div class="container mt-3">
//                                 <div class="text-center">
//                                     <img src="${course.image_url}" width="500px"/>
//                                 </div>
//                             </div>
//                             <div class="container mt-3">
//                                 <div class="text-center">
//                                     <h2><b>Overview</b></h2>
//                                 </div>
//                                 <div>${course.html_description}</div>
//                             </div>
//                     `;
//                     courseDetailDiv.append(courseHtml);
//                 } else {
//                     console.error('Error fetching course detail:', response.message);
//                 }
//             },
//             error: function(error) {
//                 console.error('Error fetching course detail:', error);
//             }
//         });
//     }

//     // Call the functions when the document is ready
//     fetchCourses()

//     // Check if the URL contains a task ID and fetch its detail
//     var courseId = window.location.href.split('/').pop();
    
//     if (!isNaN(courseId)) {
//         fetchCourseDetail(courseId);
//     }
// });

