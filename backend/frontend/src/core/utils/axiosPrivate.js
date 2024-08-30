import axios from "axios"

let API_URL = 'http://localhost:8001/api/'

const apiPrivate = axios.create({
  baseURL: API_URL,
  withCredentials: true,
  credentials: "include",
  headers: {
      "Content-Type": "application/json",
  }});

apiPrivate.interceptors.request.use((config) => {
  return config;
});

apiPrivate.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    if (error.response.status === 401) {
      var response = await axios.post(
        API_URL + 'auth/token/refresh/',
        {},
      { withCredentials: true, }
      )
      .catch((err) => {
        return Promise.reject(err);
      });
      if(response && response.data){
        return axios(error.config);

      }
      else{
        return Promise.reject(error);
      }
    } else {
      return Promise.reject(error);
    }
  }
);

export default (apiPrivate);