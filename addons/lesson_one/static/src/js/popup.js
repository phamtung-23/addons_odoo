// odoo.define('lesson_one.alert', function (require) {
//     var core = require('web.core');
//     alert(core._t('This is a test notification'));
//     return {}
//  });
$(document).ready(function() {
    // Define the URL of the API endpoint
    var apiUrl = '/api/tasks';

    // AJAX call to fetch tasks data
    $.ajax({
        url: apiUrl,
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            if (response.status === 'success') {
                var taskData = response.data;
                var taskListDiv = $('#task-list');

                // Loop through the task data and render it
                for (var i = 0; i < taskData.length; i++) {
                    var task = taskData[i];
                    var taskHtml = `
                        <div class="col-md-4">
                            <div class="card mb-4">
                                <div class="card-body">
                                    <h5 class="card-title">${task.title}</h5>
                                    <p class="card-text">${task.description}</p>
                                    <p class="card-text">Priority: ${task.priority}</p>
                                    <p class="card-text">Stage: ${task.stage}</p>
                                    <p class="card-text">Deadline: ${task.date_deadline}</p>
                                </div>
                            </div>
                        </div>
                    `;
                    taskListDiv.append(taskHtml);
                }
            }
        },
        error: function(error) {
            console.error('Error fetching tasks:', error);
        }
    });
});