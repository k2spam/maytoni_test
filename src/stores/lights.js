import { defineStore } from "pinia"
import mockLightsData from './../mocks/lights.json'

export const useLightsStore = defineStore('lights', {
    state: () => ({
        lights: [],
        filtered: [],
        selected: [],
        isNew: false,
        loading: false,
        error: null,
    }),
    actions: {
        async fetchLights(){
            try {
                const fakeRequest = new Promise((resolve) => {
                    this.loading = true
                    setTimeout(() => {
                        resolve(mockLightsData)
                    }, 3000);
                })
                
                this.lights = await fakeRequest
                this.filterLigths()
                this.loading = false
                
            }
            catch(e) {
                this.error = e
            }
        },
        filterLigths(){
            this.filtered = this.lights
            if(this.isNew) 
                this.filtered = this.filtered.filter(v => v.status === 'new')
        }
    }
})