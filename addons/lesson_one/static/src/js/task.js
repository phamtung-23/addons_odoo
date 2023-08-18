odoo.define('lesson_one.tasks_template', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    // DOM ready
    $(document).ready(function () {
        var taskId = 1;  // Replace with the actual task ID

        // Call the API using AJAX
        ajax.jsonRpc('/api/tasks', 'call', {})
            .then(function (data) {
                if (data.status === 'success') {
                    var taskData = data.data;
                    renderTaskInfo(taskData);
                } else {
                    console.error('Error:', data.message);
                }
            })
            .catch(function (error) {
                console.error('AJAX Error:', error);
            });
    });

    function renderTaskInfo(taskData) {
        // TODO: Render task data on the UI
        // For example:
        console.log(taskData);
        // $('#task-title').text(taskData.title);
        // $('#task-description').text(taskData.description);
        // $('#task-priority').text(taskData.priority);
        // ...
    }

});
