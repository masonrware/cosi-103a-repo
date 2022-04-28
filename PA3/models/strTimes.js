'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;

var strTimesSchema = Schema( {
    strTimes: [String]
  } );

module.exports = mongoose.model( 'strTimes', strTimesSchema );
