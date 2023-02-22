/* tslint:disable */
/* eslint-disable */
/**
 * PrismAgent OpenAPI specification
 * OpenAPI specification for Decentralized Identifiers (DID) Operations
 *
 * The version of the OpenAPI document: 0.1.0
 * Contact: atala-coredid@iohk.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface PublicKeyJwk
 */
export interface PublicKeyJwk {
    /**
     * 
     * @type {string}
     * @memberof PublicKeyJwk
     */
    crv?: string;
    /**
     * 
     * @type {string}
     * @memberof PublicKeyJwk
     */
    x?: string;
    /**
     * 
     * @type {string}
     * @memberof PublicKeyJwk
     */
    y?: string;
    /**
     * 
     * @type {string}
     * @memberof PublicKeyJwk
     */
    kty: string;
    /**
     * 
     * @type {string}
     * @memberof PublicKeyJwk
     */
    kid?: string;
}

/**
 * Check if a given object implements the PublicKeyJwk interface.
 */
export function instanceOfPublicKeyJwk(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "kty" in value;

    return isInstance;
}

export function PublicKeyJwkFromJSON(json: any): PublicKeyJwk {
    return PublicKeyJwkFromJSONTyped(json, false);
}

export function PublicKeyJwkFromJSONTyped(json: any, ignoreDiscriminator: boolean): PublicKeyJwk {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'crv': !exists(json, 'crv') ? undefined : json['crv'],
        'x': !exists(json, 'x') ? undefined : json['x'],
        'y': !exists(json, 'y') ? undefined : json['y'],
        'kty': json['kty'],
        'kid': !exists(json, 'kid') ? undefined : json['kid'],
    };
}

export function PublicKeyJwkToJSON(value?: PublicKeyJwk | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'crv': value.crv,
        'x': value.x,
        'y': value.y,
        'kty': value.kty,
        'kid': value.kid,
    };
}
