'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = Schema.Types.ObjectId;

var perProject = Schema( {
  userId: ObjectId,
  title: String,
  description:String,
  finishedOn: Date,
  github: String
} );

module.exports = mongoose.model( 'project', perProject );
