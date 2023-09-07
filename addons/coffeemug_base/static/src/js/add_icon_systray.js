/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
class SystrayIcon extends Component { 
    setup() {   
        super.setup(...arguments);   
        this.action = useService("action"); 
    } 
}
  
SystrayIcon.template = "systray_icon";
export const systrayItem = { Component: SystrayIcon,};
registry.category("systray").add("SystrayIcon", systrayItem, { sequence: 1 });