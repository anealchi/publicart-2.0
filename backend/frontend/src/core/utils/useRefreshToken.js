import { api } from "./axios";
import useUserStore from "@/modules/authentication/store/userStore";

export default function useRefreshToken() {
    const user = useUserStore()

    const refresh = async () => {
        const response = await api.post('/refresh-token')
        user.accessToken = response.data['access_token']
        user.csrfToken = response.headers["x-csrftoken"]
    }

    return refresh
}