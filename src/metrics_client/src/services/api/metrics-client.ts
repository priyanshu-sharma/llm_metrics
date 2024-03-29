// import { httpPost} from "../http";
import axios from "axios";
const METRICS_API_URL = "http://127.0.0.1:8000";

export const uploadPrompt = (
  files: string,
  metrics: string,
  prompt: string
) => {
  var formData = new FormData();
  formData.append("file", files);
  formData.append("prompt", prompt);
  formData.append("metrics", metrics);
  formData.append("llm_models", "CHAT_GPT");
  return axios.post(
    `${METRICS_API_URL}/api/evaluation_domain/v1/upload_file/`,
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );
};

export const getRating = (limit: number) => {
  return axios.get(`${METRICS_API_URL}/api/evaluation_domain/v1/rating/`, {
    headers: {
      "Content-Type": "application/json",
    },
    params: {
        limit: limit
    }
  });
};
