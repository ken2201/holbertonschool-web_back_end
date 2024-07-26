/* eslint-disable */
import {default as signUpUser} from './4-user-promise.js';
import {default as uploadPhoto} from './5-photo-reject.js';

export default async function handleProfileSignup(firstName, lastName, fileName) {
    const userData = await signUpUser(firstName, lastName).then((data) => ({
        status: 'fulfilled',
        value: data
    }));

    const photoData = await uploadPhoto(fileName).catch((err) => ({
        status: 'rejected',
        value: err.toString()
    }));

    return Promise.resolve([userData, photoData]);
}
