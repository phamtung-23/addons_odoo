/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.courseOpen = publicWidget.Widget.extend({
    selector: '.course-open',
    start(){
      let courseOpen = this.$target.find('#course_open_row')
      
      if(courseOpen){
        this._rpc({
          route: '/api/courses',
          params:{}
        }).then(courses=>{
          let html = ``
          courses.forEach(course => {
            html += `
                <div class="col-3 p-2">
                  <div class="card w-100">
                      <div class="card-img-top">
                          <a href="/course/${course.id}">
                              <img class="image-main rounded" src="data:image/png;base64,${course.image}" style="
                              width: 100%;
                              object-fit: cover;"/>
                          </a>
                      </div>
                      <div class="card-body" id="card_body">
                          <a href="/course/${course.id}">
                              <div class="card-title fs-6">${course.name}</div>
                          </a>
                          <div class = "mt-1" id="tags">
                              <p class="badge bg-danger">${course.type_of_course}</p>
                              <p class="badge bg-success">${course.level_of_course}</p>
                          </div>
                          <p class="card-text fs-6">With ${course.number_of_lesson} lessons</p>
                      </div>
                  </div>
                </div>`
          });
          courseOpen.html(html)
        })
      }
    }
})

export default publicWidget.registry.courseOpen;