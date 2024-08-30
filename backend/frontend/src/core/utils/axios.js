import axios from "axios"

let API_URL = 'http://localhost:8001/api/'

const api = axios.create({
    baseURL: API_URL,    
    withCredentials: true,
    headers: {
        "Content-Type": "application/json",
    }
});

export default (api);