import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);

client.on('connect', () => console.log('Redis client connected to the server'));

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

const setNewSchool = async (schoolName, value) => {
  await client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  const val = await getAsync(schoolName);
  console.log(val);
};

(async () => {
  try {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
  } catch (err) {
    console.error('Error:', err);
  }
})();
