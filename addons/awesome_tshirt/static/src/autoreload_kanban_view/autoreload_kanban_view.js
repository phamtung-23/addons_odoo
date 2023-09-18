/** @odoo-module */

import { registry } from "@web/core/registry";
import { KanbanController } from "@web/views/kanban/kanban_controller";
import { kanbanView } from "@web/views/kanban/kanban_view";
import { useInterval } from "../utils";

class AutoReloadKanbanController extends KanbanController {
    setup() {
        super.setup();
        useInterval(()=>{
            this.model.load()
            console.log('AutoReloadKanbanController');
        }, 30000);
    }
}

const AutoReloadKanbanView = {
    ...kanbanView,
    Controller: AutoReloadKanbanController,
}

registry.category("views").add("autoreloadkanban", AutoReloadKanbanView);