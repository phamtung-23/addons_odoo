/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { patch } from "@web/core/utils/patch";


patch(WebClient.prototype, "coffeemug_base.WebClient", {
    setup() {
            this._super.apply(this, arguments);
            this.title.setParts({ zopenerp: "SIRS" }); 
    }
});