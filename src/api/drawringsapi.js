import axios from 'axios';

// replace this with your LAN IP  
const BASE_URL = 'http://192.168.0.205:8000'; // room wifi
// const BASE_URL = 'http://10.249.42.17:8000'; // eduroam

export async function uploadDrawing(photoUri) {
  console.log('Uploading drawing from uri:', photoUri);

  const formData = new FormData();
  formData.append('file', {
    uri: photoUri,
    type: 'image/jpeg',
    name: 'drawing.jpg',
  });

  const response = await axios.post(`${BASE_URL}/extract-character`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    timeout: 60000,
  });

  return response.data;
}
